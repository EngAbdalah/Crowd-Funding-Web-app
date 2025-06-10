// src/pages/ReportDetails.js
import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import api from '../services/api';
import {
    Box,
    Typography,
    Paper,
    CircularProgress,
    Button,
    MenuItem,
    Select,
    FormControl,
    InputLabel,
    Grid,
    Alert,
    Divider,
    Chip,
} from '@mui/material';

const ReportDetails = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const [report, setReport] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [status, setStatus] = useState('');
    const [updateSuccess, setUpdateSuccess] = useState(false);

    useEffect(() => {
        const fetchReport = async () => {
            try {
                const response = await api.get(`/reports/${id}/`);
                setReport(response.data);
                setStatus(response.data.status);
            } catch (err) {
                setError(err.response?.data?.message || 'Failed to fetch report');
            } finally {
                setLoading(false);
            }
        };

        fetchReport();
    }, [id]);

    const handleStatusChange = async () => {
        try {
            await api.patch(`/reports/${id}/`, { status });
            setUpdateSuccess(true);
            setTimeout(() => setUpdateSuccess(false), 3000);
            // Refresh report data
            const response = await api.get(`/reports/${id}/`);
            setReport(response.data);
        } catch (err) {
            setError(err.response?.data?.message || 'Failed to update report');
        }
    };

    const handleDelete = async () => {
        if (window.confirm('Are you sure you want to delete this report?')) {
            try {
                await api.delete(`/reports/${id}/`);
                navigate('/reports', { replace: true });
            } catch (err) {
                setError(err.response?.data?.message || 'Failed to delete report');
            }
        }
    };

    const getStatusColor = (status) => {
        switch (status) {
            case 'pending':
                return 'default';
            case 'reviewed':
                return 'primary';
            case 'dismissed':
                return 'secondary';
            default:
                return 'default';
        }
    };

    if (loading) return <CircularProgress />;
    if (error) return <Typography color="error">{error}</Typography>;
    if (!report) return <Typography>Report not found</Typography>;

    return (
        <Box sx={{ padding: '20px' }}>
            <Typography variant="h4" gutterBottom>
                Report Details
            </Typography>

            <Button
                variant="outlined"
                onClick={() => navigate('/reports')}
                sx={{ mb: 2 }}
            >
                Back to Reports
            </Button>

            {updateSuccess && (
                <Alert severity="success" sx={{ mb: 2 }}>
                    Report status updated successfully!
                </Alert>
            )}

            <Paper sx={{ padding: '20px', mb: 2 }}>
                <Grid container spacing={3}>
                    <Grid item xs={12} md={6}>
                        <Typography variant="h6" gutterBottom>
                            Basic Information
                        </Typography>

                        <Grid container spacing={2}>
                            <Grid item xs={6}>
                                <Typography variant="subtitle2">Report ID</Typography>
                                <Typography>{report.id}</Typography>
                            </Grid>
                            <Grid item xs={6}>
                                <Typography variant="subtitle2">Comment ID</Typography>
                                <Typography>{report.comment}</Typography>
                            </Grid>
                            <Grid item xs={12}>
                                <Typography variant="subtitle2">Reason</Typography>
                                <Typography>{report.reason}</Typography>
                            </Grid>
                        </Grid>

                        <Divider sx={{ my: 3 }} />

                        <Typography variant="h6" gutterBottom>
                            Status Information
                        </Typography>
                        <Grid container spacing={2}>
                            <Grid item xs={6}>
                                <Typography variant="subtitle2">Current Status</Typography>
                                <Chip
                                    label={report.status}
                                    color={getStatusColor(report.status)}
                                    size="small"
                                />
                            </Grid>
                            <Grid item xs={6}>
                                <Typography variant="subtitle2">Reviewed</Typography>
                                <Typography>
                                    {report.is_reviewed ? (
                                        <Chip label="Yes" color="success" size="small" />
                                    ) : (
                                        <Chip label="No" color="error" size="small" />
                                    )}
                                </Typography>
                            </Grid>
                        </Grid>
                    </Grid>

                    <Grid item xs={12} md={6}>
                        <Typography variant="h6" gutterBottom>
                            Timestamps
                        </Typography>
                        <Grid container spacing={2}>
                            <Grid item xs={12}>
                                <Typography variant="subtitle2">Created At</Typography>
                                <Typography>
                                    {new Date(report.created_at).toLocaleString()}
                                </Typography>
                            </Grid>
                        </Grid>

                        <Divider sx={{ my: 3 }} />

                        <Typography variant="h6" gutterBottom>
                            Update Status
                        </Typography>
                        <FormControl fullWidth sx={{ mt: 1, mb: 2 }}>
                            <InputLabel>Status</InputLabel>
                            <Select
                                value={status}
                                label="Status"
                                onChange={(e) => setStatus(e.target.value)}
                                size="small"
                            >
                                <MenuItem value="pending">Pending</MenuItem>
                                <MenuItem value="reviewed">Reviewed</MenuItem>
                                <MenuItem value="dismissed">Dismissed</MenuItem>
                            </Select>
                        </FormControl>

                        <Box sx={{ display: 'flex', gap: 2 }}>
                            <Button
                                variant="contained"
                                onClick={handleStatusChange}
                                disabled={status === report.status}
                            >
                                Update Status
                            </Button>
                            <Button
                                variant="contained"
                                color="error"
                                onClick={handleDelete}
                            >
                                Delete Report
                            </Button>
                        </Box>
                    </Grid>
                </Grid>
            </Paper>
        </Box>
    );
};

export default ReportDetails;